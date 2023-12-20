"""empty message

Revision ID: 5df5ad62bd5a
Revises: e8324aa42d9e
Create Date: 2023-11-25 19:03:36.929712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5df5ad62bd5a'
down_revision: Union[str, None] = 'e8324aa42d9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('is_true', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('test_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('question_answers')
    # ### end Alembic commands ###