wrd_fun_body = word_fun(df, "body")
wrd_fun_body_sw = word_fun(df, "body_sw")

df["body_sw_stem"] = df["body_sw"].apply(stem_fun)