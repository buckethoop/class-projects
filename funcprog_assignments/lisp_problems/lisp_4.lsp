;; This buffer is for text that is not saved, and for Lisp evaluation.
;; To create a file, visit it with C-x C-f and enter text in its buffer.

(defun sum-even-odd (numbers)
  (let ((even-sum 0)
        (odd-sum 0)
        (index 0))
    (dolist (num numbers)
      (if (evenp index)
          (setq even-sum (+ even-sum num))
          (setq odd-sum (+ odd-sum num)))
      (setq index (1+ index)))
    (cons even-sum odd-sum)))
