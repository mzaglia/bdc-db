"""empty message

Revision ID: 4a2287967b77
Revises: c1ca0249cb60
Create Date: 2020-01-15 11:59:48.082132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a2287967b77'
down_revision = 'c1ca0249cb60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('grs_schemas', sa.Column('crs', sa.String(length=400), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('grs_schemas', 'crs')
    # ### end Alembic commands ###
