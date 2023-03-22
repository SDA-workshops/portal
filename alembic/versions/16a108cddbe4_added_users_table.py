"""added users table

Revision ID: 16a108cddbe4
Revises: 
Create Date: 2023-03-22 17:56:01.960173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16a108cddbe4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('fullname', sa.String(length=50), nullable=True),
        sa.Column('lastname', sa.String(length=50), nullable=True),
        sa.Column('nickname', sa.String(length=50), nullable=False),
        sa.Column('email', sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('nickname')
    )


def downgrade() -> None:
    op.drop_table('users')
