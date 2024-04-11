def zabran_kradezi_okapu(material_okapu):
    materialy = ["plast","ocel","hliník"]
    if material_okapu in materialy:
        print( "Okap se nevyplatí ukrást")
    else:
        print("Ber to moreee")
zabran_kradezi_okapu("ocel")