!python -m pip install --upgrade pip setuptools wheel
!python -m pip install lbry-libtorrent
!apt install python3-libtorrent

import libtorrent as lt

ses = lt.session()
ses.listen_on(6881, 6891)
downloads = []