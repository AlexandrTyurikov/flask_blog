"""empty message

Revision ID: 5d18d56640b2
Revises: ec07ec7c6c02
Create Date: 2020-01-13 06:55:19.108735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d18d56640b2'
down_revision = 'ec07ec7c6c02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles_user',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_constraint('user_role_id_fkey', 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('user_role_id_fkey', 'user', 'role', ['role_id'], ['id'])
    op.drop_table('roles_user')
    # ### end Alembic commands ###
