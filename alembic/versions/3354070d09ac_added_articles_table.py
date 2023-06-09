"""added articles table

Revision ID: 3354070d09ac
Revises: f8b15e6352f4
Create Date: 2023-03-22 18:50:17.124306

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3354070d09ac'
down_revision = 'f8b15e6352f4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=70), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    # ### end Alembic commands ###
