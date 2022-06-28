from modules import module as mod


def main():
    DF_PULLS = mod.get_pulls(mod.BASE_URL, mod.KEY, mod.OWNER, mod.REPO, mod.PULLS, mod.SEARCH, mod.STATE, mod.USERNAME, mod.API_TOKEN, mod.field_list1)
    DF_STATUS = mod.df_status(DF_PULLS, mod.BASE_URL, mod.KEY, mod.OWNER, mod.REPO, mod.COMMITS, mod.USERNAME, mod.API_TOKEN, mod.field_list2)
    DF_CSV = mod.create_csv(DF_STATUS, mod.field_sort1, mod.field_name1)
    DF_CSV
      

if __name__ == '__main__':
    main()
