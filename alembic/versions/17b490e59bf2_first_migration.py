"""First Migration

Revision ID: 17b490e59bf2
Revises: 
Create Date: 2023-08-08 18:55:54.352790

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17b490e59bf2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('appointments',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('provider', sa.String(), nullable=False),
    sa.Column('appointment_datetime', sa.DateTime(), nullable=True),
    sa.Column('chief_complaint', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='public'
    )
    op.create_table('patients',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('contact_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='public'
    )
    op.create_table('insurances',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('patient_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['public.patients.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='public'
    )
    op.create_table('referrals',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('referring_doctor', sa.String(), nullable=False),
    sa.Column('patient_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['public.patients.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    schema='public'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('referrals', schema='public')
    op.drop_table('insurances', schema='public')
    op.drop_table('patients', schema='public')
    op.drop_table('appointments', schema='public')
    # ### end Alembic commands ###
