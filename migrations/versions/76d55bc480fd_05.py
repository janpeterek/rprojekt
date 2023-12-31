"""05

Revision ID: 76d55bc480fd
Revises: 40d74879164b
Create Date: 2023-10-29 14:15:22.731000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76d55bc480fd'
down_revision = '40d74879164b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visit', schema=None) as batch_op:
        batch_op.drop_column('stars')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('visit', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stars', sa.VARCHAR(length=1), nullable=False))

    # ### end Alembic commands ###
