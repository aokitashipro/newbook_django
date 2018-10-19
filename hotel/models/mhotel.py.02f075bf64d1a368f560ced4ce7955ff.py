from django.db import models

class mHotel(models.Model):
  class Meta:
    db_table = 'mHotel'

"""
sample

  title = models.CharField(verbose_name='タイトル', max_length=255)
  price = models.IntegerField(verbose_name='価格', null=True, blank=Type)

"""

	hotel_id = models.CharField(max_length=7)
  chain_id = models.IntegerField

# ホテル名は日本語名だけ？
  hotel_name = models.CharField(max_length=100)

	login_id = models.CharField(max_length=32)
	password =  models.CharField(max_length=60)

	room_calc_type 
	person_num_check_type

# calc float
	round_function

	is_use_request = models.BooleanField(default=True)
	is_include_tax = models.BooleanField(default=True)
	is_include_service_charge = models.BooleanField(default=False)

# bath tax
	bath_tax = models.PositiveSmallIntegerField
	child_bath_tax = models.PositiveSmallIntegerField

#	宿泊税 バリエーション

# 軽減税率 バリエーション


	room_closing_out_day = models.PositiveSmallIntegerField 
	room_closing_out_hour = models.PositiveSmallIntegerField
	room_closing_out_minutes = models.PositiveSmallIntegerField
	opt_closing_out_day = models.PositiveSmallIntegerField
	opt_closing_out_hour = models.PositiveSmallIntegerField
	opt_closing_out_minutes = models.PositiveSmallIntegerField
	cancellable_day = models.PositiveSmallIntegerField
	checkin_time_from_hour = models.PositiveSmallIntegerField
	checkin_time_from_minutes = models.PositiveSmallIntegerField
	checkin_time_to_hour = models.PositiveSmallIntegerField
	checkin_time_to_minutes = models.PositiveSmallIntegerField

# 子供設定はここに必要？デフォルト設定か
	calc_value_child 
	calc_value_baby_meal_bed
	calc_value_baby_meal
	calc_value_baby_bed
	calc_value_baby

# 日帰り許可？
	is_allow_another_daily_room = models.BooleanField(default=True)

# 食事の数を許可？
	is_allow_select_meal_num = models.BooleanField(default=True)

	email = models.EmailField(max_length=254)

# キャンポリ以降だとメール送信したりしたい
	cancel_policy

# メンバー？
	is_use_member = models.BooleanField(default=True)

# わからない
	member_agree 

# ここは不要かも
	header = models.TextField ヘッダー
	footer = models.TextField フッター

	is_use_tema  = models.BooleanField(default=False)
	is_use_lincoln  = models.BooleanField(default=False)
	is_use_neppan  = models.BooleanField(default=Flase)
	tema_password  = models.CharField(max_length=60)
	lincoln_password = models.CharField(max_length=60)
	neppan_password = models.CharField(max_length=60)
	insert_date 
	update_date
	is_deleted 

# グーグルアナリティクス
# 

  def __str__(self):
    return self.title
