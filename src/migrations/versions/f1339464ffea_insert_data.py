"""insert data

Revision ID: f1339464ffea
Revises: a2156a9d55bd
Create Date: 2025-05-16 22:44:44.485844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1339464ffea'
down_revision: Union[str, None] = 'a2156a9d55bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 1)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 2)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 3)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 4)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 5)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 6)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 7)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 8)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 9)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 10)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 11)""")
    op.execute("""INSERT INTO users (role_admin, admin_id) VALUES (TRUE, 12)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 1)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 2)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 3)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 4)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 5)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 6)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 7)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 8)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 9)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 10)""")
    op.execute("""INSERT INTO users (role_admin, team_id) VALUES (FALSE, 11)""")

    op.execute("""INSERT INTO img (name) VALUES ('img0')""")
    op.execute("""INSERT INTO img (name) VALUES ('img1')""")
    op.execute("""INSERT INTO img (name) VALUES ('img2')""")
    op.execute("""INSERT INTO img (name) VALUES ('img3')""")
    op.execute("""INSERT INTO img (name) VALUES ('img4')""")
    op.execute("""INSERT INTO img (name) VALUES ('img5')""")
    op.execute("""INSERT INTO img (name) VALUES ('img6')""")
    op.execute("""INSERT INTO img (name) VALUES ('img7')""")
    op.execute("""INSERT INTO img (name) VALUES ('img8')""")
    op.execute("""INSERT INTO img (name) VALUES ('img9')""")
    op.execute("""INSERT INTO img (name) VALUES ('img10')""")
    op.execute("""INSERT INTO img (name) VALUES ('img11')""")
    op.execute("""INSERT INTO img (name) VALUES ('img12')""")


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""DELETE FROM users""")
    op.execute("""DELETE FROM img""")
