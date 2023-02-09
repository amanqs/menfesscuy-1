import os

api_id = int(os.environ.get("API_ID", "#"))
api_hash = os.environ.get("API_HASH", "#")
bot_token = os.environ.get("BOT_TOKEN", "#")
# =========================================================== #

db_url = os.environ.get("DB_URL", "#")
db_name = os.environ.get("DB_NAME", "telegram") #bisa diganti sesuai kebutuhan
# =========================================================== #

channel_1 = int(os.environ.get("CHANNEL_1", "#"))
channel_2 = int(os.environ.get("CHANNEL_2", "#")) #untuk group comentar user
channel_log = int(os.environ.get("CHANNEL_LOG", "#"))
# =========================================================== #

id_admin = int(os.environ.get("ID_ADMIN", "907544310"))
# =========================================================== #

batas_kirim = int(os.environ.get("BATAS_KIRIM", "5"))
batas_talent = int(os.environ.get("BATAS_TALENT", "10"))
batas_daddy_sugar = int(os.environ.get("BATAS_DADDY_SUGAR", "10"))
batas_moansgirl = int(os.environ.get("BATAS_MOANSGIRL", "10"))
batas_moansboy = int(os.environ.get("BATAS_MOANSBOY", "10"))
batas_gfrent = int(os.environ.get("BATAS_GFRENT", "10"))
batas_bfrent = int(os.environ.get("BATAS_BFRENT", "10"))
# =========================================================== #

biaya_kirim = int(os.environ.get("BIAYA_KIRIM", "10"))
biaya_talent = int(os.environ.get("BIAYA_TALENT", "80"))
biaya_daddy_sugar = int(os.environ.get("BIAYA_DADDY_SUGAR", "70"))
biaya_moansgirl = int(os.environ.get("BIAYA_MOANSGIRL", "60"))
biaya_moansboy = int(os.environ.get("BIAYA_MOANSBOY", "50"))
biaya_gfrent = int(os.environ.get("BIAYA_GFRENT", "40"))
biaya_bfrent = int(os.environ.get("BIAYA_BFRENT", "30"))
# =========================================================== #

hastag = os.environ.get("HASTAG", "#Girl #Boy #Ask #Find #Spill #Story").replace(" ", "|").lower()
# =========================================================== #

pic_boy = os.environ.get("PIC_BOY", "https://telegra.ph/file/a35541745ce3e3c4f5178.jpg")
pic_girl = os.environ.get("PIC_GIRL", "https://telegra.ph/file/55efbdcad8af18a84500e.jpg")
# =========================================================== #

pesan_join = os.environ.get("PESAN_JOIN", "Tidak Dapat Diakses Harap Join Terlebih Dahulu")
start_msg = os.environ.get("START_MSG", "Hai {mention} 🌱\n\n<b>Alter FWB Bot</b> adalah Bot Auto Post, Semua Pesan Yang Kamu Kirim Akan Masuk Ke Channel @DuniaVirtualMenfess Secara Anonymous. Untuk Bantuan Ketik /help")

gagalkirim_msg = os.environ.get("GAGAL_KIRIM", """
{mention}, Pesan Mu Gagal Terkirim Silahkan Gunakan Hashtag Berikut:

#Boy / #Girl (Untuk Mencari Pasangan, Teman , Partner FWB)
#Ask (Untuk Bertanya)
#Story (Untuk Berbagi Cerita)
#Spill (Untuk Spill Masalah)
#Find (Untuk Mencari Pasangan, Teman, Partner FWB)
""")
