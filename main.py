from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "6738197512:AAFx5QdGhj9O1n5TBxvDY7k76Ijb2xf8sGc"  # Remplacez par le token que vous avez obtenu

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Bienvenue dans votre assistant virtuel! Envoyez-moi vos PDF.")

def handle_pdf(update: Update, context: CallbackContext) -> None:
    # Traitement du PDF ici
    file_id = update.message.document.file_id
    new_file = context.bot.get_file(file_id)
    new_file.download('document.pdf')
    update.message.reply_text("PDF reçu avec succès!")

def main() -> None:
    updater = Updater(TOKEN)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.document, handle_pdf))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
  
