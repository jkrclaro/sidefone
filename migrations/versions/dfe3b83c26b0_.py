"""empty message

Revision ID: dfe3b83c26b0
Revises: 8580ff9ee573
Create Date: 2019-07-03 11:43:46.774072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfe3b83c26b0'
down_revision = '8580ff9ee573'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('uid', sa.String(length=255), nullable=True))
    op.drop_column('products', 'unique_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('unique_id', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('products', 'uid')
    # ### end Alembic commands ###