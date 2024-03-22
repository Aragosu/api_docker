"""asyncpg DB

Revision ID: 83c6ec5deecd
Revises: 
Create Date: 2024-03-15 00:13:40.284511

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '83c6ec5deecd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('role_id', sa.Integer(), nullable=True),
                    sa.Column('hashed_password', sa.String(), nullable=True),
                    sa.Column('is_active', sa.Boolean(), nullable=False),
                    sa.Column('is_superuser', sa.Boolean(), nullable=False),
                    sa.Column('is_verified', sa.Boolean(), nullable=False),
                    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
                    sa.PrimaryKeyConstraint('id')
    )
    op.execute('''INSERT INTO role VALUES (1,'user'),(2,'admin')''')
    list_users = ['195', '1010', '7438', '30323', '30349', '1019900']
    for i in list_users:
        test_password = '$argon2id$v=19$m=65536,t=3,p=4$e9DEx5PDQMp82KCcWEKmrA$KN0+VrbugVqy9BS1gA8oBNRT1l4E63kqxm6rV5LGcg4'
        op.execute(f'''INSERT INTO public.user VALUES ({i},'test{i}@mail.com','test_user{i}',1,'{test_password}',True,False,False)''')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###
