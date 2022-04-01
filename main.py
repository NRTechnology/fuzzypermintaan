# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    permintaan = {
        'min': 1000,
        'max': 5000
    }

    persediaan = {
        'min': 100,
        'max': 600
    }

    produksi = {
        'min': 2000,
        'max': 7000
    }

    kasus = {
        'permintaan': 4000,
        'persediaan': 300
    }

    # Rule base
    # rule 1, jika permintaan turun dan persediaan banyak produksi berkurang
    # rule 2, jika permintaan turun dan persediaan sedikit produksi berkurang
    # rule 3, jika permintaan naik dan persediaan banyak produksi bertambah
    # rule 4, jika permintaan naik dan persediaan sedikit produksi bertambah
    # berapa harus produksi jika permintaan 4000 dan persediaan 300

    # algo permintaan turun
    # (max permintaan-permintaan) bagi (max permintaan - min permintaan)
    permintaan_turun = (permintaan['max'] - kasus['permintaan']) / (permintaan['max'] - permintaan['min'])
    print(permintaan_turun)

    # algo permintaan Naik
    # (permintaan-min permintaan) bagi (max permintaan - min permintaan)
    permintaan_naik = (kasus['permintaan'] - permintaan['min']) / (permintaan['max'] - permintaan['min'])
    print(permintaan_naik)

    # algo persediaan turun
    # (max persediaan-persediaan) bagi (max persediaan - min persediaan)
    persediaan_turun = (persediaan['max'] - kasus['persediaan']) / (persediaan['max'] - persediaan['min'])
    print(persediaan_turun)

    # algo persediaan Naik
    # (persediaan-min persediaan) bagi (max persediaan - min persediaan)
    persediaan_naik = (kasus['persediaan'] - persediaan['min']) / (persediaan['max'] - persediaan['min'])
    print(persediaan_naik)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
