"""asyncpg DB

Revision ID: 83c6ec5deecd
Revises: 
Create Date: 2024-03-15 00:13:40.284511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean, MetaData
#from src.auth.models import role


# revision identifiers, used by Alembic.
revision: str = '83c6ec5deecd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operation',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.String(), nullable=True),
                    sa.Column('figi', sa.String(), nullable=True),
                    sa.Column('instrument_type', sa.String(), nullable=True),
                    sa.Column('date', sa.TIMESTAMP(), nullable=True),
                    sa.Column('type', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
#    op.execute('''INSERT INTO role VALUES (1,'user'),(2,'admin')''')
#    op.commit()
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operation')
#    op.drop_table('user')
#    op.drop_table('role')
    # ### end Alembic commands ###
