a
    ]��`�  �                   @   s�   d Z dZdZdZdZdZdZdZdd	lZdd	l	Z	dd	l
Z
zdd	lZW nF ey�   ed
� e�d� ed� e	�d� ed� dd	lZY n0 dd� Ze�  d	S )z[0mz[31m�[1;32mz[33mz[34mz[35mz[36mz[37m�    Nz5[35m  [[33m*[35m][31m Required Module Not Found !�   z([35m  [[33m*[35m][1;32m Installing !zpip install yt2mp3down z+[35m  [[33m*[35m][35m Module Installed!c                  C   s�   t �d� t �d� td� td� td� z8td�} td� t�| � td� td� t �d	� W n   td
� t �d� Y n0 d S )N�clearz(figlet -f smmono9  "  YT2MP3 " | lolcat � z[31m#CODED BY DEVIL MASTERz+[35m  [[33m*[35m][36m Enter The Link : r   z4[35m  [[33m*[35m][35m Downloading... Successed. z4[35m  [[33m*[35m][33m Press Enter To Continue : zbash singme.shz([35m  [[33m*[35m][31m Internal Error�exit)�os�system�print�input�
yt2mp3downZmp3)�link� r   �	yt2mp3.py�menu   s    


r   )�W�R�G�O�B�P�CZGR�timer   �sysr   �ModuleNotFoundErrorr	   �sleepr   r   r   r   r   r   �<module>   s&   

