from mongoengine import *


class Checkpoint(EmbeddedDocument):
    """
    A MongoEngine EmbeddedDocument containing:
        distance: MongoEngine float field, required, (checkpoint distance in kilometers),
		open_time: MongoEngine datetime field, required, (checkpoint opening time),
		close_time: MongoEngine datetime field, required, (checkpoint closing time).
    """
    distance = IntField(required = True)
    location = StringField(required = False)
    open_time = StringField(required = True)
    close_time = StringField(required = True)
    pass


class Brevet(Document):
    """
    A MongoEngine document containing:
		length: MongoEngine float field, required
		begin_date: MongoEngine datetime field, required
		checkpoints: MongoEngine list field of Checkpoints, required
    """
    length = FloatField(required = True)
    begin_date = StringField(required = True)
    checkpoints = EmbeddedDocumentListField(Checkpoint, required = True)
    pass
