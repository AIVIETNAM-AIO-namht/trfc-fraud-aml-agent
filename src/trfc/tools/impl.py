"""5 tool của TRFC — chủ sở hữu: B. Mốc: CP2 (chạy với tool giả) → CP3 (thật).

Bảng tool (DE_TAI_TRFC_Agent.md §5.2):

  search_policy               đọc    uỷ quyền cho A (trfc.rag.search)
  get_transactions            đọc    đọc data/state.db
  get_account_risk_status     đọc    BƯỚC VERIFY BẮT BUỘC
  freeze_account_temporarily  GHI    ghi data/state.db
  flag_suspicious_tx          GHI    ghi data/state.db

QUY TẮC SẮT (yêu cầu 2.6): tool lỗi trả chuỗi `"Error: ..."`, KHÔNG raise.
Agent phải thấy lỗi và tự điều chỉnh, không được làm chết run.

ponytail: để trống có chủ đích. Đây là phần bị vấn đáp nặng nhất ("chứng minh
agent thực sự dùng kết quả tool") nên B phải viết tay.
"""

from trfc.tools.schemas import Ack, Chunk, RiskStatus, Transaction


def get_transactions(account_id: str, date_from: str, date_to: str) -> list[Transaction]:
    """Giao dịch của tài khoản trong khoảng ngày (YYYY-MM-DD). B cài đặt."""
    raise NotImplementedError("B — CP2.")


def get_account_risk_status(account_id: str) -> RiskStatus:
    """Đọc trạng thái rủi ro HIỆN TẠI từ state.db. B cài đặt — đây là bước verify."""
    raise NotImplementedError("B — CP2.")


def freeze_account_temporarily(account_id: str, reason: str) -> Ack:
    """Ghi: khoá tạm thời tài khoản. B cài đặt."""
    raise NotImplementedError("B — CP2.")


def flag_suspicious_tx(tx_id: str, reason: str) -> Ack:
    """Ghi: đánh dấu giao dịch đáng ngờ. B cài đặt."""
    raise NotImplementedError("B — CP2.")


def search_policy(query: str, k: int = 5, tier: int | None = None,
                  mode: str = "hybrid") -> list[Chunk]:
    """Uỷ quyền cho A — B không sửa logic ở đây (PHAN_CONG.md §7 quy tắc 3)."""
    from trfc.rag.search import search_policy as _impl

    return _impl(query=query, k=k, tier=tier, mode=mode)
