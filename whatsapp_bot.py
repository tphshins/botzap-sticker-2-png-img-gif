import pywhatkit as kit

def handle_message(message):
    # Verifica se a mensagem contém o comando '/toimg'
    if "/toimg" in message:
        try:
            # Usa a biblioteca pywhatkit para converter o sticker em imagem PNG
            kit.sticker_to_png(r'caminho_para_o_sticker', r'caminho_para_salvar_imagem.png')
            return "Aqui está a imagem PNG do sticker."
        except Exception as e:
            return f"Erro ao converter sticker para imagem PNG: {e}"

    # Verifica se a mensagem contém o comando '/togif'
    elif "/togif" in message:
        try:
            # Usa a biblioteca pywhatkit para converter o sticker animado em GIF
            kit.sticker_to_gif(r'caminho_para_o_sticker', r'caminho_para_salvar_animacao.gif')
            return "Aqui está o GIF animado do sticker."
        except Exception as e:
            return f"Erro ao converter sticker para GIF: {e}"

    # Caso nenhum comando seja reconhecido
    else:
        return "Comando inválido. Use '/toimg' para converter sticker em PNG ou '/togif' para GIF."

# Exemplo de uso
mensagem_do_usuario = input("Digite sua mensagem: ")
resposta_bot = handle_message(mensagem_do_usuario)
print(resposta_bot)
