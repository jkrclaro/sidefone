"""empty message

Revision ID: db93216ca178
Revises: 55b6371f13dd
Create Date: 2019-07-15 14:51:49.043984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db93216ca178'
down_revision = '55b6371f13dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('variants', sa.Column('title', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('variants', 'title')
    # ### end Alembic commands ###