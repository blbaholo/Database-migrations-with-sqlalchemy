"""rename_chatname_column

Revision ID: 21068c7b95ab
Revises: fa4e435b827d
Create Date: 2023-04-12 22:53:50.084393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21068c7b95ab'
down_revision = 'fa4e435b827d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "recruits", "chatname", nullable=False, new_column_name="rocketchat_user"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "recruits", "rocketchat_user", nullable=False, new_column_name="chatname"
    )
    # ### end Alembic commands ###
