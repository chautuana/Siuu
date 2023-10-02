from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image

class MyApp(App):
    def build(self):
        # Chia kích thước cửa sổ ứng dụng thành 1/3 kích thước ban đầu
        Window.size = (1170, 2532)
        
        self.icon = "dai_ca.jpg"
        self.title = "App Của An"
        
        layout = RelativeLayout()
        
        # Đặt kích thước của Button phù hợp với cửa sổ mới
        button1 = Button(
            text='LICK ME ???',
            size_hint=(None, None),
            size=(0.5 * 390, 0.5 * 844),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            background_color='#FFFF66',
            color='#FF0000',
            font_size=24
        )
        
        
        # Tạo Image widget để hiển thị ảnh
        image = Image(source='khi_ngu.jpg', allow_stretch=True)
        image.size_hint = (1, 1)
        
        #image.pos_hint={'center_x':0.5,'center_y':0.5}
        image.opacity = 0  # Ẩn ảnh ban đầu
        def bat_nut(instance):
            image.opacity = 1

        # Liên kết hàm xử lý sự kiện với sự kiện nhấn nút 

        button1.bind(on_press=bat_nut)
        
        # Thêm Button và Image vào layout cha
        layout.add_widget(button1)
        layout.add_widget(image)

        return layout

if __name__ == '__main__':
    MyApp().run()
