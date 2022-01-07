"""create-tag-posts

Revision ID: b40d7a12f47b
Revises: b5bd3dd2824e
Create Date: 2021-05-18 16:29:48.753344

"""
from alembic import op
import sqlalchemy as sa
from models import Tag


# revision identifiers, used by Alembic.
revision = 'b40d7a12f47b'
down_revision = 'b5bd3dd2824e'
branch_labels = None
depends_on = None


def upgrade():
  op.create_table(
  'tag_posts',
  sa.Column('id', sa.Integer, primary_key=True),
  sa.Column('tag_id', sa.Integer),
  sa.Column('post_id', sa.Integer)
)
  seed() 
def seed():
 
  op.bulk_insert(Tag.__table__,
      [
          {"tag_id":1,"post_id":1},
      
          {"tag_id":2,"post_id":2}
      ]
  )


def downgrade():
    op.drop_table('tag_posts')

