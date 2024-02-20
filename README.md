# Discord Status Changer

Este script te permite cambiar el estado de tu cuenta de Discord automáticamente a partir de los estados definidos en un archivo de texto.

## Requisitos

- Python 3.x instalado
- Paquetes necesarios: `requests`

Puedes instalar los paquetes necesarios ejecutando el siguiente comando:


## Uso

1. Clona este repositorio o descarga el archivo `discord_status_changer.py`.
2. Crea un archivo `config.json` con la siguiente estructura:

```json
{
  "token": "tu_token_de_discord",
  "clear_enabled": true,
  "clear_interval": 15,
  "sleep_interval": 3
}
