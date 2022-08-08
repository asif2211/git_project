from git_project.locator import Display


class Login(Display):

    def display_remove(self):
        print(self.display_data())
    def get_user_inof(self):
        print('user info')

object = Login()
object.display_remove()