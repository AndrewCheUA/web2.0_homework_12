"""Init

Revision ID: 261d0da9d536
Revises: e204ac06b4b5
Create Date: 2023-02-25 19:24:48.254948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '261d0da9d536'
down_revision = 'e204ac06b4b5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    # ### end Alembic commands ###