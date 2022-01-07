"""create-posts

Revision ID: c693caa69c1f
Revises: bf65aee2866b
Create Date: 2021-05-18 16:26:46.095803

"""
from alembic import op
import sqlalchemy as sa
from models import Post

# revision identifiers, used by Alembic.
revision = 'c693caa69c1f'
down_revision = 'bf65aee2866b'
branch_labels = None
depends_on = None


def seed():
 
  op.bulk_insert(Post.__table__,
      [
          {"title": "user1lol",
          "description":"user1lol",
          "category_id":1},
      
          {"title": "user2lol",
          "description":"user2lol",
          "category_id":2}
      ]
  )
def upgrade():
    op.create_table(
    'posts',
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('title', sa.String, nullable=False),
    sa.Column('description', sa.String, nullable=False),
    sa.Column('category_id', sa.Integer)
  )
    seed()



def downgrade():
    op.drop_table('categories')

