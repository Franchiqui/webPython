import deepl

def traductor(request_data):
    # Extraer los datos de la solicitud
    translate_text, target_lang = request_data.split('&')
    translate_text = translate_text.split('=')[1]
    target_lang = target_lang.split('=')[1]

    auth_key = "a4341cbe-a8bd-4ac2-97e4-6bce2574cf8a:fx"  # Reemplaza con tu clave
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(translate_text, target_lang=target_lang)
    return result.text

