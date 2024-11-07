from kandinsky import KandinskyAPI

def main():
    api_key = "your api key"
    secret_key = "your secret key"
    prompt = input()
    # Инициализация клиента API
    api = KandinskyAPI(api_key, secret_key)
    
    # Получение ID модели
    model_id = api.get_model()
    
    # Запрос генерации изображения
    uuid = api.generate(prompt, model_id)
    images = api.check_generation(uuid)
    
    if images:
        # Сохранение сгенерированного изображения на устройство
        api.save_image(images[0], "output_image.png")
    else:
        print("Не удалось сгенерировать изображение")
  

if __name__ == "__main__":
    main()
