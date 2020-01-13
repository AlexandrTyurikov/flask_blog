"""empty message

Revision ID: db05c2709707
Revises: d0965cfe1e27
Create Date: 2020-01-10 12:42:28.631552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db05c2709707'
down_revision = 'd0965cfe1e27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_user')
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'post', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'user_id')
    op.create_table('post_user',
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name='post_user_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='post_user_user_id_fkey')
    )
    # ### end Alembic commands ###