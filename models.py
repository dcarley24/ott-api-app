from extensions import db

# All database models are now defined in this file.

video_tags = db.Table('video_tags',
    db.Column('video_id', db.Integer, db.ForeignKey('videos.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(300), nullable=False)
    poster_path = db.Column(db.String(300), nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True, default=0)
    content_type = db.Column(db.String(50), default='movie')
    tags = db.relationship('Tag', secondary=video_tags, backref=db.backref('videos', lazy='dynamic'))

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Channel(db.Model):
    __tablename__ = 'channels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo_path = db.Column(db.String(300), nullable=True)
    channel_type = db.Column(db.String(50), nullable=False, default='manual')
    rule_tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), nullable=True)
    rule_tag = db.relationship('Tag', foreign_keys=[rule_tag_id])

class ChannelSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    channel_id = db.Column(db.Integer, db.ForeignKey('channels.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'), nullable=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('ads.id'), nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    channel = db.relationship('Channel', backref=db.backref('schedule_entries', lazy=True, cascade="all, delete-orphan"))
    video = db.relationship('Video')

class Ad(db.Model):
    __tablename__ = 'ads'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    file_path = db.Column(db.String(300), nullable=False)
    duration_seconds = db.Column(db.Integer, nullable=False, default=15)
