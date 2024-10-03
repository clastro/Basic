PAPS_AF_Single['Filename'] = (
    PAPS_AF_Single['Screening_No'].astype(str) + '_' + 
    PAPS_AF_Single['ID'].astype(str).apply(lambda x: x.zfill(8)) + '_' +
    PAPS_AF_Single['AFIB_New'].str.split('-').str[0] + 
    PAPS_AF_Single['AFIB_New'].str.split('-').str[1] + 
    PAPS_AF_Single['AFIB_New'].str.split('-').str[2] + 
    '.xml'
)

# zfill -> zero fill
