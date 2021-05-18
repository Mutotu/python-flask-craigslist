"""create-categories

Revision ID: bf65aee2866b
Revises: 
Create Date: 2021-05-18 16:25:43.046779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf65aee2866b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'categories',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String, nullable=False, unique=True)
  )


def downgrade():
    op.drop_table('categories')
