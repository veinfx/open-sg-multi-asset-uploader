import shotgun_api3

SERVER_PATH = "https://url.shotgrid.autodesk.com"
SCRIPT_NAME = "script name"
SCRIPT_KEY = "script key"

sg = shotgun_api3.Shotgun(SERVER_PATH,
                          script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)


class SgMapping:
    """
    로컬에 있는 파일을 샷그리드의 Asset 에 upload 하기위해 shotgun_api3 를 맵핑한 api 이다.
    """
    def __init__(self):
        pass

    def select_get_project(self, project_name):
        """
        유저가 선택한 콤보박스의  프로젝트이름으로 프로젝트의 dict 를 구하는 함수이다.
        """
        user_project = sg.find("Project", [["name", "is", project_name]], [])

        for dict in user_project:
            user_project.extend(dict)
            return user_project[0]

    def get_active_project(self):
        """
        active 된 프로젝트 목록을 get 하는 함수이다.
        """
        projects = sg.find("Project", [["sg_status", "is", "Active"]], ["name"])
        project_dict = sorted(list(set([project["name"] for project in projects])))
        return project_dict

    def get_asset_template(self):
        """
        schema_field_read 를 사용하여 정해진 asset template list를 구하는 함수이다.
        """
        entity_fields = sg.schema_field_read("Asset", "sg_asset_type")
        asset_types = entity_fields["sg_asset_type"]["properties"]["valid_values"]["value"]
        asset_type_list = sorted(list(set([asset_type for asset_type in asset_types])))
        return asset_type_list

    def asset_create(self, project, asset_type, asset_name):
        """
        ui 에서 유저가 선택한 project(combobox),asset_type(tree), asset_name(local file basename),
        path(local file dirpath)를 받아서 샷그리드 api (sg.create)로 샷그리드에 asset을 만드는 함수이다.
        """
        entity_type = "Asset"
        asset_data = {"code": asset_name, "project": project, "sg_asset_type": asset_type}
        sg.create(entity_type, asset_data)
