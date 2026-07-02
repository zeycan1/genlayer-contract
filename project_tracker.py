# v0.2.16
# { "Depends": "py-genlayer:1jb45aa0ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh0jpz09h6" }

from genlayer import *

class ProjectTracker(gl.Contract):
    project_data: str

    def __init__(self, initial_data: str):
        self.project_data = initial_data

    @gl.public.view
    def get_project_data(self) -> str:
        return self.project_data

    @gl.public.write
    def update_project_data(self, new_data: str) -> None:
        self.project_data = new_data
