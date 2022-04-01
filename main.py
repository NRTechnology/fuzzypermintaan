def fuzzy_union(nilai_a, nilai_b):
    if nilai_a < nilai_b:
        return nilai_a
    return nilai_b


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

    # algo permintaan Naik
    # (permintaan-min permintaan) bagi (max permintaan - min permintaan)
    permintaan_naik = (kasus['permintaan'] - permintaan['min']) / (permintaan['max'] - permintaan['min'])

    # algo persediaan sedikit
    # (max persediaan-persediaan) bagi (max persediaan - min persediaan)
    persediaan_sedikit = (persediaan['max'] - kasus['persediaan']) / (persediaan['max'] - persediaan['min'])

    # algo persediaan banyak
    # (persediaan-min persediaan) bagi (max persediaan - min persediaan)
    persediaan_banyak = (kasus['persediaan'] - persediaan['min']) / (persediaan['max'] - persediaan['min'])

    alpred_z = []
    # rule 1
    apred1 = fuzzy_union(permintaan_turun, persediaan_banyak)
    z1 = produksi['max'] - (apred1 * (produksi['max'] - produksi['min']))
    alpred_z.append({
        'apred': apred1,
        'z': z1
    })

    # rule 2
    apred2 = fuzzy_union(permintaan_turun, persediaan_sedikit)
    z2 = produksi['max'] - (apred2 * (produksi['max'] - produksi['min']))
    alpred_z.append({
        'apred': apred2,
        'z': z2
    })

    # rule 3
    apred3 = fuzzy_union(permintaan_naik, persediaan_banyak)
    z3 = produksi['min'] + (apred3 * (produksi['max'] - produksi['min']))
    alpred_z.append({
        'apred': apred3,
        'z': z3
    })

    # rule 3
    apred4 = fuzzy_union(permintaan_naik, persediaan_sedikit)
    z4 = produksi['min'] + (apred4 * (produksi['max'] - produksi['min']))
    alpred_z.append({
        'apred': apred4,
        'z': z4
    })

    pembilang_rerata = 0
    for data in alpred_z:
        pembilang_rerata += (data['apred'] * data['z'])

    penyebut_rerata = 0
    for data in alpred_z:
        penyebut_rerata += data['apred']

    rerata = pembilang_rerata / penyebut_rerata
    print("Produksi " + str(int(rerata)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
