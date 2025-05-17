from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass


class UserBase(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(nullable=True)
    role_admin: Mapped[bool] = mapped_column(default=False)
    admin_id: Mapped[int] = mapped_column(nullable=True)
    team_id: Mapped[int] = mapped_column(nullable=True)
    persons: Mapped[str] = mapped_column(nullable=True)
    in_progress: Mapped[bool] = mapped_column(default=False)
    feedback_id: Mapped[int] = mapped_column(nullable=True)


class CallBase(Base):
    __tablename__ = 'calls'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    admin_id: Mapped[int] = mapped_column(nullable=False)
    team_id: Mapped[int] = mapped_column(nullable=False)
    team_feedback: Mapped[int] = mapped_column(nullable=True)
    admin_feedback: Mapped[str] = mapped_column(default="")


class ImgBase(Base):
    __tablename__ = 'img'

    name: Mapped[str] = mapped_column(primary_key=True)
    id: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[str] = mapped_column(nullable=True)
