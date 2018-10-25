import uuid
import time
from django.db import transaction
from django.db.utils import IntegrityError

#まだ使いこなせてない
def retried_insert(instance, pkdict={}):
    """
    インスタンスの内容をDBに登録します。
    もし、PK重複により登録失敗したら、PKを再生成して登録を試みます。
    Args:
        instance: 登録対象のインスタンス
        pkdict: PKのディクショナリ
            これはテスト時に、重複エラーを発生させるために用意してあります。
    """
    max_retries = 9  # 最大再試行回数
    for idx in range(max_retries + 1):
        try:
            with transaction.atomic(savepoint=True):
                instance.pk = pkdict.get(idx) or uuid.uuid4()
                instance.save(force_insert=True)
                break
        except IntegrityError:
            time.sleep(0.1)
    else:
        # インスタンスの登録ができなかった場合は例外を投げます。
        raise IntegrityError('DBに登録できませんでした。[%s].' % type(instance))