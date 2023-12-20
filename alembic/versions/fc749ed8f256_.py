"""empty message

Revision ID: fc749ed8f256
Revises: 5df5ad62bd5a
Create Date: 2023-11-25 20:15:20.318170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc749ed8f256'
down_revision: Union[str, None] = '5df5ad62bd5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('chat_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    # ### end Alembic commands ###
