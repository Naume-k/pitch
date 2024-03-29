"""Initial Migration

Revision ID: 74bcec919017
Revises: 9237b9209b50
Create Date: 2019-09-24 11:16:11.916329

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '74bcec919017'
down_revision = '9237b9209b50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('category', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reviews')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('movie_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('image_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('movie_review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='reviews_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reviews_pkey')
    )
    op.drop_table('pitches')
    # ### end Alembic commands ###
