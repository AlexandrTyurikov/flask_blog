"""empty message

Revision ID: ec07ec7c6c02
Revises: db05c2709707
Create Date: 2020-01-13 06:50:00.514334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec07ec7c6c02'
down_revision = 'db05c2709707'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles_user')
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user', 'role', ['role_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.create_table('roles_user',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='roles_user_role_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='roles_user_user_id_fkey')
    )
    # ### end Alembic commands ###
