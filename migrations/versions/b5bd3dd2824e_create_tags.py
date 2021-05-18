"""create-tags

Revision ID: b5bd3dd2824e
Revises: c693caa69c1f
Create Date: 2021-05-18 16:28:26.988625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5bd3dd2824e'
down_revision = 'c693caa69c1f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'tags',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String, nullable=False, unique=True)
  )


def downgrade():
    op.drop_table('tags')

