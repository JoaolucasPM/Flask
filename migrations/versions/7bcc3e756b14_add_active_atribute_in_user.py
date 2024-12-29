"""Add active atribute in user

Revision ID: 7bcc3e756b14
Revises: 17fbd20b7b28
Create Date: 2024-12-29 19:44:31.677234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bcc3e756b14'
down_revision = '17fbd20b7b28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=False))
        batch_op.drop_column('username')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('active')

    # ### end Alembic commands ###
