from google.colab import files

source = files.upload()
params = {
    "save_path": "/content/drive/My Drive/Torrent",
    "ti": lt.torrent_info(list(source.keys())[0]),
}
downloads.append(ses.add_torrent(params))