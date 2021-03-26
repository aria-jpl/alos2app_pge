import papermill as pm
import os
from pathlib import Path

python_script_path = Path(__file__).absolute()
pge_path = python_script_path.parents[0]
os.environ['PGE_DIRECTORY'] = str(pge_path.absolute())

PGE_DIRECTORY = os.environ['PGE_DIRECTORY']
NB_DIRECTORY = f'{PGE_DIRECTORY}/notebooks'


def print_header(header):
    header_formatted = ('##############\n'
                        f'{header}\n'
                        '##############'
                       )
    print(header_formatted)

notebook_name = '1_Get_Metadata.ipynb'
print_header(notebook_name)
pm.execute_notebook(f'{NB_DIRECTORY}/{notebook_name}',
                    f'{notebook_name}'
                    )

notebook_name = '2_Downloading_the_DEM.ipynb'
print_header(notebook_name)
pm.execute_notebook(f'{NB_DIRECTORY}/{notebook_name}',
                    f'{notebook_name}'
                    )

notebook_name = '3_Water_Mask.ipynb'
print_header(notebook_name)
pm.execute_notebook(f'{NB_DIRECTORY}/{notebook_name}',
                    f'{notebook_name}'
                    )

notebook_name = '4_SAR_Processing.ipynb'
print_header(notebook_name)
pm.execute_notebook(f'{NB_DIRECTORY}/{notebook_name}',
                    f'{notebook_name}'
                    )

notebook_name = '5_Packaging.ipynb'
print_header(notebook_name)
pm.execute_notebook(f'{NB_DIRECTORY}/{notebook_name}',
                    f'{notebook_name}'
                    )
