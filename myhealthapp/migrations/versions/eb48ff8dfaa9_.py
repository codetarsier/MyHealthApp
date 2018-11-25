"""empty message

Revision ID: eb48ff8dfaa9
Revises: cc805ab1bc28
Create Date: 2018-11-25 13:06:04.252642

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb48ff8dfaa9'
down_revision = 'cc805ab1bc28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=False))
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['username'])
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
