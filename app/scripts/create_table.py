from app.infrastructure.database.db_config import engine
from app.infrastructure.database.base import Base
from app.infrastructure.database.models import credor_model, precatorio_model

Base.metadata.create_all(engine)