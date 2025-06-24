from flask import Blueprint, jsonify, url_for
from datetime import datetime

# Import models from the new models.py file
from models import Video, Tag, Channel, video_tags

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/channels', methods=['GET'])
def get_channels():
    channels = Channel.query.all()
    channel_list = []
    for channel in channels:
        channel_list.append({
            'id': channel.id,
            'name': channel.name,
            'type': channel.channel_type,
            'play_url': url_for('api.get_channel_playback', channel_id=channel.id, _external=True)
        })
    return jsonify(channels=channel_list)


@api_bp.route('/channel/play/<int:channel_id>', methods=['GET'])
def get_channel_playback(channel_id):
    channel = Channel.query.get_or_404(channel_id)

    if channel.channel_type == 'manual':
        return jsonify(error="Manual channel API playback not yet implemented"), 501

    elif channel.channel_type == 'virtual':
        if not channel.rule_tag_id:
            return jsonify(error="Virtual channel is not configured with a rule"), 404

        videos_with_rule_tag = Video.query.join(video_tags).join(Tag).filter(Tag.id == channel.rule_tag_id).all()

        if not videos_with_rule_tag:
            return jsonify(error="No videos found for this channel's rule"), 404

        total_duration_seconds = sum(v.duration_seconds for v in videos_with_rule_tag if v.duration_seconds)
        if total_duration_seconds == 0:
            return jsonify(error="Playlist has zero duration"), 404

        now_utc = datetime.utcnow()
        seconds_into_day = (now_utc - now_utc.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()
        current_loop_position = seconds_into_day % total_duration_seconds

        seek_offset = 0
        current_video = None
        time_accumulator = 0
        sorted_videos = sorted(videos_with_rule_tag, key=lambda v: v.id)

        for video in sorted_videos:
            video_duration = video.duration_seconds
            if time_accumulator + video_duration > current_loop_position:
                current_video = video
                seek_offset = current_loop_position - time_accumulator
                break
            time_accumulator += video_duration

        if not current_video:
            current_video = sorted_videos[0]
            seek_offset = 0

        video_filename = current_video.file_path.split('/')[-1]

        playback_data = {
            'channel_name': channel.name,
            'video_title': current_video.title,
            'video_url': url_for('uploaded_video_file', filename=video_filename, _external=True),
            'start_offset_seconds': seek_offset
        }
        return jsonify(playback_data)

    return jsonify(error="Unknown channel type"), 400
