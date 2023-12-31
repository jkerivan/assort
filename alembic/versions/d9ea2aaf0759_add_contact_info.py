"""Add contact info

Revision ID: d9ea2aaf0759
Revises: bd555dad1aa2
Create Date: 2023-08-09 21:51:54.860495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd9ea2aaf0759'
down_revision: Union[str, None] = 'bd555dad1aa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('insurances_patient_id_fkey', 'insurances', type_='foreignkey')
    op.create_foreign_key(None, 'insurances', 'patients', ['patient_id'], ['id'], source_schema='public', referent_schema='public')
    op.drop_constraint('referrals_patient_id_fkey', 'referrals', type_='foreignkey')
    op.create_foreign_key(None, 'referrals', 'patients', ['patient_id'], ['id'], source_schema='public', referent_schema='public')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'referrals', schema='public', type_='foreignkey')
    op.create_foreign_key('referrals_patient_id_fkey', 'referrals', 'patients', ['patient_id'], ['id'])
    op.drop_constraint(None, 'insurances', schema='public', type_='foreignkey')
    op.create_foreign_key('insurances_patient_id_fkey', 'insurances', 'patients', ['patient_id'], ['id'])
    # ### end Alembic commands ###
